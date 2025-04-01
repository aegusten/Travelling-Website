document.addEventListener("DOMContentLoaded", function () {
  // Open modal
  document.querySelectorAll("[data-modal-open]").forEach(button => {
    button.addEventListener("click", () => {
      const targetSelector = button.getAttribute("data-modal-open");
      const modal = document.querySelector(targetSelector);
      if (modal) {
        modal.classList.add("active");
      }
    });
  });

  // Close modal
  document.querySelectorAll("[data-close-modal]").forEach(button => {
    button.addEventListener("click", () => {
      const modal = button.closest(".modal");
      if (modal) {
        modal.classList.remove("active");
      }
    });
  });

  // Close modal on overlay click
  document.querySelectorAll(".modal-overlay").forEach(overlay => {
    overlay.addEventListener("click", () => {
      const modal = overlay.closest(".modal");
      if (modal) {
        modal.classList.remove("active");
      }
    });
  });

  // Toggle password visibility
  document.querySelectorAll(".toggle-password-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const targetInput = document.querySelector(btn.getAttribute("data-target"));
      if (targetInput) {
        targetInput.type = targetInput.type === "password" ? "text" : "password";
        btn.querySelector("i").classList.toggle("fa-eye");
        btn.querySelector("i").classList.toggle("fa-eye-slash");
      }
    });
  });
});
