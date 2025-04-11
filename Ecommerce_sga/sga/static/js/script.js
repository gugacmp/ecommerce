/* script.js */
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('form-produto');
    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Produto salvo com sucesso!');
      });
    }
  });
  