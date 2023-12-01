document.addEventListener('DOMContentLoaded', function () {
    const dataSelect = document.getElementById('data-select');
    const plotDiv = document.getElementById('plot-div');

    dataSelect.addEventListener('change', function () {
        const selectedData = dataSelect.value;
        fetch('/plot', {
            method: 'POST',
            body: new URLSearchParams({ selected_data: selectedData }),
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        })
            .then(response => response.json())
            .then(data => {
                Plotly.newPlot(plotDiv, data.data, data.layout);
            });
    });

    // Initialize the chart with default data
    dataSelect.dispatchEvent(new Event('change'));
});

                const xValues = [100,200,300,400,500,600,700,800,900,1000];
                
                new Chart("myChart", {
                  type: "line",
                  data: {
                    labels: xValues,
                    datasets: [{ 
                      data: [860,1140,1060,1060,1070,1110,1330,2210,7830,2478],
                      borderColor: "red",
                      fill: false
                    }, { 
                      data: [1600,1700,1700,1900,2000,2700,4000,5000,6000,7000],
                      borderColor: "green",
                      fill: false
                    }, { 
                      data: [300,700,2000,5000,6000,4000,2000,1000,200,100],
                      borderColor: "blue",
                      fill: false
                    }]
                  },
                  options: {
                    legend: {display: false}
                  }
                });

                function scrollFunction() {
                    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                      document.getElementById("navbar").style.top = "0";
                    } else {
                      document.getElementById("navbar").style.top = "-50px";
                    }
                  }

                  function openNav() {
                    document.getElementById("mySidenav").style.width = "250px";
                    document.getElementById("main").style.marginLeft = "250px";
                    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
                  }
            
                  function closeNav() {
                    document.getElementById("mySidenav").style.width = "0";
                    document.getElementById("main").style.marginLeft = "0";
                    document.body.style.backgroundColor = "white";
                  }
            
                  function openNavTable() {
                    document.getElementById("table").style.width = "250px";
                    document.getElementById("main").style.marginBottom= "550px";
                    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
                  }
            
                  function closeNavTable() {
                    document.getElementById("table").style.width = "0";
                    document.getElementById("main").style.marginBottom = "0";
                    document.body.style.backgroundColor = "white";
                  }
            
                  function canvas() {
                    const xValues = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000];
                    new Chart("myChart", {
                      type: "line",
                      data: {
                        labels: xValues,
                        datasets: [{
                          data: [860, 1140, 1060, 1060, 1070, 1110, 1330, 2210, 7830, 2478],
                          borderColor: "red",
                          fill: false
                        }, {
                          data: [1600, 1700, 1700, 1900, 2000, 2700, 4000, 5000, 6000, 7000],
                          borderColor: "green",
                          fill: false
                        }, {
                          data: [300, 700, 2000, 5000, 6000, 4000, 2000, 1000, 200, 100],
                          borderColor: "blue",
                          fill: false
                        }]
                      },
                      options: {
                        legend: {
                          display: false
                        }
                      }
                    });
                  }