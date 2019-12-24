var quizScoresDiv = document.getElementById('quizScores').getContext('2d');
var quizScores = new Chart(quizScoresDiv, {
    type: 'bar',
    data: {
      labels: ['0/8', '1/8', '2/8', '3/8', '4/8', '5/8', '6/8', '7/8', '8/8'],
      datasets: [{
        label: '# who scored',
        data: [39, 68, 98, 104, 68, 16, 9, 0 , 0],
        backgroundColor: [
          'rgba(255, 117, 125, 0.2)',
          'rgba(0, 241, 118, 0.2)',
          'rgba(255, 117, 125, 0.2)',
          'rgba(0, 241, 118, 0.2)',
          'rgba(255, 117, 125, 0.2)',
          'rgba(0, 241, 118, 0.2)',
          'rgba(255, 117, 125, 0.2)',
          'rgba(0, 241, 118, 0.2)',
          'rgba(255, 117, 125, 0.2)'
        ],
        borderColor: [
          'rgba(255, 117, 125, 1)',
          'rgba(0, 241, 118, 1)',
          'rgba(255, 117, 125, 1)',
          'rgba(0, 241, 118, 1)',
          'rgba(255, 117, 125, 1)',
          'rgba(0, 241, 118, 1)',
          'rgba(255, 117, 125, 1)',
          'rgba(0, 241, 118, 1)',
          'rgba(255, 117, 125, 1)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true,
            fontColor: 'rgba(225, 225, 225, 0.7)'
          }
        }],
        xAxes: [{
          ticks: {
            fontColor: 'rgba(225, 225, 225, 0.7)'
          }
        }],
      },
      legend: {
        display: false,
    }
  }
});

var partyAffiliationDiv = document.getElementById('partyAffiliation').getContext('2d');
var partyAffiliation = new Chart(partyAffiliationDiv, {
    type: 'doughnut',
    data: {
      labels:['Brexit','Change UK','Conservative','Green','Labour','Liberal Democrat','Unknown'],
      datasets: [{
        data: [12, 6, 15, 68, 162, 123, 37],
        backgroundColor: [
          'rgba(18, 182, 207, 0.3)',
          'rgba(0, 0, 0, 0.3)',
          'rgba(0, 135, 220, 0.3)',
          'rgba(0, 116, 95, 0.3)',
          'rgba(213, 0, 0, 0.3)',
          'rgba(253, 187, 48, 0.3)',
          'rgba(255, 255, 255, 0.2)'
        ],
        borderColor: [
          'rgba(255, 255, 255, 0.7)',
          'rgba(255, 255, 255, 0.7)',
          'rgba(255, 255, 255, 0.7)',
          'rgba(255, 255, 255, 0.7)',
          'rgba(255, 255, 255, 0.7)',
          'rgba(255, 255, 255, 0.7)',
          'rgba(255, 255, 255, 0.7)',
          'rgba(255, 255, 255, 0.7)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      legend: {
        labels: {
          fontColor: 'rgba(255, 255, 255, 0.7)'
        }
      }
    }
});