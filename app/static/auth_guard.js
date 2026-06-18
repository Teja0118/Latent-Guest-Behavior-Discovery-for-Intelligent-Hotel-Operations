function checkAuthentication() {

    const token =
        localStorage.getItem(
            "access_token"
        );

    if (!token) {

        window.location.replace(
            "/login-page"
        );
    }
}

document.addEventListener(
    "DOMContentLoaded",
    checkAuthentication
);

window.addEventListener(
    "pageshow",
    checkAuthentication
);