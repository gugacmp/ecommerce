const data = {
    labels: ['Enviados', 'Entregues', 'Aguardando envio'],
    datasets: [{
      data: [10, 25, 5],
      backgroundColor: ['#36a2eb', '#4caf50', '#ffca28']
    }]
  };
  
  new Chart(document.getElementById('grafico-logistica'), {
    type: 'pie',
    data: data
  });
  