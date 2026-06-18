
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
async function registerUser() {

    const body = {

        name:
            document.getElementById(
                "name"
            ).value,

        email:
            document.getElementById(
                "email"
            ).value,

        password:
            document.getElementById(
                "password"
            ).value
    };

    const response = await fetch(

        "/register",

        {

            method: "POST",

            headers: {

                "Content-Type":
                    "application/json"
            },

            body:
                JSON.stringify(body)
        }
    );

    const data =
        await response.json();

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

    const response = await fetch(

        "/login",

        {

            method: "POST",

            body: formData
        }
    );

    const data =
        await response.json();

    console.log(data);

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

    showToast(
        "Login Successful ✓"
    );


    console.log(

        "TOKEN STORED:",

        localStorage.getItem(
            "access_token"
        )
    );

    window.location.href =
        "/";
}

function logout() {

    localStorage.removeItem(
        "access_token"
    );

    window.location.href =
        "/login-page";
}
