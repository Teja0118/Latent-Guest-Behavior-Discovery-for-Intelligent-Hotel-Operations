function showToast(
    message,
    type = "success"
) {

    const toast =
        document.createElement(
            "div"
        );

    toast.className =
        `toast toast-${type}`;

    toast.innerHTML =
        message;

    document.body.appendChild(
        toast
    );

    setTimeout(() => {

        toast.remove();

    }, 3000);
}

function togglePassword(
    inputId,
    element
) {

    const input =
        document.getElementById(
            inputId
        );

    const icon =
        element.querySelector("i");

    if (
        input.type === "password"
    ) {

        input.type = "text";

        icon.classList.remove(
            "fa-eye"
        );

        icon.classList.add(
            "fa-eye-slash"
        );

    } else {

        input.type = "password";

        icon.classList.remove(
            "fa-eye-slash"
        );

        icon.classList.add(
            "fa-eye"
        );
    }
}

function checkPasswordStrength() {

    const password =
        document.getElementById(
            "password"
        )?.value || "";

    const bar =
        document.getElementById(
            "strength-bar"
        );

    const text =
        document.getElementById(
            "strength-text"
        );

    if (!bar || !text) return;

    let score = 0;

    if (password.length >= 8) score++;
    if (/[A-Z]/.test(password)) score++;
    if (/[a-z]/.test(password)) score++;
    if (/\d/.test(password)) score++;
    if (
        /[!@#$%^&*(),.?":{}|<>]/
            .test(password)
    ) score++;

    if (score <= 2) {

        bar.style.width = "30%";
        bar.style.background = "#ef4444";

        text.innerHTML =
            "Weak Password";

    } else if (score <= 4) {

        bar.style.width = "70%";
        bar.style.background = "#f59e0b";

        text.innerHTML =
            "Medium Password";

    } else {

        bar.style.width = "100%";
        bar.style.background = "#10b981";

        text.innerHTML =
            "Strong Password";
    }
}

async function registerUser() {

    const password =
        document.getElementById(
            "password"
        ).value;

    const confirmPassword =
        document.getElementById(
            "confirm_password"
        ).value;

    const errorElement =
        document.getElementById(
            "password-error"
        );

    errorElement.innerHTML = "";

    const passwordRegex =
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;

    if (
        !passwordRegex.test(
            password
        )
    ) {

        errorElement.innerHTML =
            "Password must contain minimum 8 characters, uppercase, lowercase, number and special character.";

        return;
    }

    if (
        password !== confirmPassword
    ) {

        errorElement.innerHTML =
            "Passwords do not match.";

        return;
    }

    const body = {

        name:
            document.getElementById(
                "name"
            ).value,

        email:
            document.getElementById(
                "email"
            ).value,

        password: password
    };

    const response =
        await fetch(

            "/register",

            {

                method: "POST",

                headers: {

                    "Content-Type":
                        "application/json"
                },

                body:
                    JSON.stringify(
                        body
                    )
            }
        );

    const data =
        await response.json();

    if (!response.ok) {

        showToast(
            data.detail ||
            "Registration Failed",
            "error"
        );

        return;
    }

    showToast(
        "Registration Successful ✓"
    );

    setTimeout(() => {

        window.location.href =
            "/login-page";

    }, 1500);
}

async function loginUser() {

    const formData =
        new FormData();

    formData.append(
        "username",
        document.getElementById(
            "email"
        ).value
    );

    formData.append(
        "password",
        document.getElementById(
            "password"
        ).value
    );

    const response =
        await fetch(

            "/login",

            {

                method: "POST",

                body: formData
            }
        );

    const data =
        await response.json();

    if (!response.ok) {

        showToast(

            data.detail ||
            "Login Failed",

            "error"
        );

        return;
    }

    localStorage.setItem(
        "access_token",
        data.access_token
    );

    localStorage.setItem(
        "current_user",
        JSON.stringify(data.user)
    );

    showToast(
        "Login Successful ✓"
    );

    setTimeout(() => {

        window.location.href =
            "/";

    }, 500);
}

function logout() {

    localStorage.removeItem(
        "access_token"
    );

    localStorage.removeItem(
        "current_user"
    );

    window.location.href =
        "/login-page";
}
