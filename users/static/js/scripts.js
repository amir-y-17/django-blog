document.addEventListener("DOMContentLoaded", function () {
    let uploadButton = document.getElementById("uploadButton");
    let profileImageInput = document.getElementById("profileImageInput");
    let profileImage = document.getElementById("profileImage");
    let form = document.getElementById("profileForm");

    // Clicking the upload button opens the file input
    uploadButton.addEventListener("click", function () {
        profileImageInput.click();
    });

    // Change the image when a new file is selected
    profileImageInput.addEventListener("change", function (event) {
        let file = event.target.files[0];
        if (file) {
            let reader = new FileReader();
            reader.onload = function (e) {
                profileImage.src = e.target.result; // Display the new image
            };
            reader.readAsDataURL(file);
        }
    });

    // Submit the form and send data (including image) to the server
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission

        let formData = new FormData(form);

        // Ensure the image file is included
        let file = profileImageInput.files[0];
        if (file) {
            formData.append("profile_image", file);
        }

        // Get CSRF token from the form
        let csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

        fetch("http://127.0.0.1:8000/users/edit-profile/", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": csrfToken
            }
        }).then(response => {
            if (response.ok) {
                alert("Profile updated successfully!");
                window.location.href = "http://127.0.0.1:8000/users/profile/"; // Redirect to profile page
            } else {
                alert("Something went wrong!");
            }
        }).catch(error => console.error("Error:", error));
    });
});
