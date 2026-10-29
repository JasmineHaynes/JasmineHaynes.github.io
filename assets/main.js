
document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector("nav");
  if (toggle && nav) toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
  });
  const year = document.querySelector("[data-year]");
  if (year) year.textContent = new Date().getFullYear();
  const current = location.pathname.replace(/\/+$/, "");
  document.querySelectorAll("nav a").forEach(a => {
    const href = a.getAttribute("href") || "";
    if (href.startsWith("#") && current === "") return;
    if (href && !href.startsWith("#") && current.endsWith(href.replace(/\/+$/, ""))) a.classList.add("active");
  });
});
