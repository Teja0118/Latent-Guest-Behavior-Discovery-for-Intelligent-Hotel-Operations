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

    alert(data.message);

    window.location.href =
        "/login-page";
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

        alert(
            data.detail ||
            "Login Failed"
        );

        return;
    }

    localStorage.setItem(

        "access_token",

        data.access_token
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
