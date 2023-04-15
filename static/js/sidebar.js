const shrink_btn = document.querySelector(".shrink-btn");
const search = document.querySelector(".search");
const tooltip_elements = document.querySelectorAll(".tooltip-element");
let currentUrl = window.location.href;
let activeLink = document.querySelector(`.sidebar-links a[href="${currentUrl}"]`);

shrink_btn.addEventListener("click", () => {
  document.body.classList.toggle("shrink");
  shrink_btn.classList.add("hovered");
  setTimeout(() => {
    shrink_btn.classList.remove("hovered");
  }, 500);
});

search.addEventListener("click", () => {
  document.body.classList.remove("shrink");
  search.lastElementChild.focus();
});

function showTooltip() {
  let tooltip = this.parentNode.lastElementChild;
  let spans = tooltip.children;
  let tooltipIndex = this.dataset.tooltip;
  Array.from(spans).forEach((sp) => sp.classList.remove("show"));
  spans[tooltipIndex].classList.add("show");
  tooltip.style.top = `${(100 / (spans.length * 2)) * (tooltipIndex * 2 + 1)}%`;
}

tooltip_elements.forEach((elem) => {
  elem.addEventListener("mouseover", showTooltip);
});