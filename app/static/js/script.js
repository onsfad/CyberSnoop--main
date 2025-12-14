document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('leakForm');
    const inputValue = document.getElementById('inputValue');
    const checkBtn = document.getElementById('checkBtn');
    const loader = document.getElementById('loader');
    const resultBox = document.getElementById('resultBox');
    const statusDiv = document.getElementById('status');
    const breachDetailsDiv = document.getElementById('breachDetails');
    const tipsDiv = document.getElementById('tips');
    const darkModeToggle = document.getElementById('darkModeToggle');

    // Update placeholder based on selected type
    const updatePlaceholder = () => {
        const type = document.querySelector('input[name="checkType"]:checked').value;
        if (type === 'email') {
            inputValue.placeholder = 'Enter email address';
        } else {
            inputValue.placeholder = 'Enter phone number';
        }
        clearResults();
    };

    // Clear results display
    const clearResults = () => {
        resultBox.style.display = 'none';
        statusDiv.textContent = '';
        breachDetailsDiv.textContent = '';
        tipsDiv.textContent = '';
    };

    // Email validation regex
    const validateEmail = (email) => {
        const re = /^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$/;
        return re.test(email);
    };

    // Phone validation (basic digits only, length 7-15)
    const validatePhone = (phone) => {
        const re = /^\\d{7,15}$/;
        return re.test(phone);
    };

    // Show loader
    const showLoader = () => {
        loader.style.display = 'block';
        checkBtn.disabled = true;
    };

    // Hide loader
    const hideLoader = () => {
        loader.style.display = 'none';
        checkBtn.disabled = false;
    };

    // Show results
    const showResults = (data, inputType) => {
        resultBox.style.display = 'block';
        if (data.breached) {
            statusDiv.innerHTML = `&#9888; Leaked in ${data.breach_count} breach${data.breach_count > 1 ? 'es' : ''}`;
            let breachNames = '';
            if (data.breach_details.names) {
                breachNames = data.breach_details.names.join(', ');
            }
            let breachDates = '';
            if (data.breach_details.dates) {
                breachDates = data.breach_details.dates.join(', ');
            }
            let exposedData = '';
            if (data.breach_details.exposed_data) {
                exposedData = data.breach_details.exposed_data.join(', ');
            }
            breachDetailsDiv.innerHTML = `<strong>Breach Names:</strong> ${breachNames}<br/><strong>Breach Dates:</strong> ${breachDates}<br/><strong>Exposed Data Types:</strong> ${exposedData}`;

            // Tips based on breach
            tipsDiv.innerHTML = `<strong>Tips:</strong><ul>
                <li>Change your password immediately</li>
                <li>Enable two-factor authentication</li>
                <li>Be cautious of phishing attempts</li>
            </ul>`;
        } else {
            statusDiv.textContent = 'Safe - No breaches found';
            breachDetailsDiv.textContent = '';
            tipsDiv.textContent = '';
        }
    };

    // Handle form submit
form.addEventListener('submit', async (e) => {
        e.preventDefault();
        clearResults();

        const input = inputValue.value.trim();
        const inputType = document.querySelector('input[name="checkType"]:checked').value;

        console.log('Submitting check for:', input, 'Type:', inputType);

        // Validate input
        if (inputType === 'email' && !validateEmail(input)) {
            alert('Please enter a valid email address.');
            return;
        }
        if (inputType === 'phone' && !validatePhone(input)) {
            alert('Please enter a valid phone number (digits only, 7-15 characters).');
            return;
        }

        showLoader();

        try {
            const response = await fetch('/check', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ input, type: inputType }),
            });

            console.log('Response status:', response.status);

            if (!response.ok) {
                throw new Error('Error checking breach');
            }

            const data = await response.json();
            console.log('Response data:', data);
            showResults(data, inputType);
        } catch (error) {
            console.error('Error during fetch:', error);
            alert('Error checking breach: ' + error.message);
        } finally {
            hideLoader();
        }
    });

    // Update placeholder on radio change
    document.querySelectorAll('input[name="checkType"]').forEach(radio => {
        radio.addEventListener('change', updatePlaceholder);
    });

    // Dark mode toggle
    darkModeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
    });

    // Initialize placeholder
    updatePlaceholder();
});
