const ctx = document.getElementById('graficoCanceladas').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Cancelado por cliente', 'Pagamento não aprovado'],
      datasets: [{
        label: 'Vendas Canceladas',
        data: [1, 1],  // valores de exemplo
        backgroundColor: ['#dc3545', '#ffc107'],
        borderRadius: 6,
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          display: false
        },
        title: {
          display: true,
          text: 'Motivos de Cancelamento'
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            precision: 0
          }
        }
      }
    }
  });