url = new URL(window.location.href);
pass = url.searchParams.get("pass");
document.getElementById("pass").value = pass;