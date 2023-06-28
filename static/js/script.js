// Close messages after 5 seconds
$(document).ready(function () {
    setTimeout(function () {
            let messages = document.getElementById('msg');
            let alert = new bootstrap.Alert(messages);
            alert.close();
    }, 5000);
});
