document.addEventListener("click", (e) => {
  if (e.target.matches("[data-modal-open]")) {
    const modalId = e.target.getAttribute("data-modal-open");
    const modal = document.querySelector(modalId);
    modal.classList.add("active");
  }
  if (e.target.matches("[data-close-modal]") || e.target.closest("[data-close-modal]")) {
    const modal = e.target.closest(".modal");
    const errorBox = modal.querySelector(".error-messages");
    if (errorBox) {
      errorBox.remove();
    }
    modal.classList.remove("active");
  }
  if (e.target.matches(".toggle-password-btn") || e.target.closest(".toggle-password-btn")) {
    const btn = e.target.closest(".toggle-password-btn");
    const targetSelector = btn.getAttribute("data-target");
    const passwordField = document.querySelector(targetSelector);
    if (passwordField.type === "password") {
      passwordField.type = "text";
      btn.innerHTML = '<i class="fa fa-eye-slash"></i>';
    } else {
      passwordField.type = "password";
      btn.innerHTML = '<i class="fa fa-eye"></i>';
    }
  }
});
