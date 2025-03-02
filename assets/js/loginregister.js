document.addEventListener("click", (e) => {
    // OPEN MODAL
    if (e.target.matches("[data-modal-open]")) {
      const modalId = e.target.getAttribute("data-modal-open");
      const modal = document.querySelector(modalId);
      modal.classList.add("active");
    }
  
    // CLOSE MODAL
    if (
      e.target.matches("[data-close-modal]") ||
      e.target.closest("[data-close-modal]")
    ) {
      const modal = e.target.closest(".modal");
      modal.classList.remove("active");
    }
  });
  