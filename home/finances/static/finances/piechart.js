$(function () {
    var $chartsContainer = $("#chartsContainer")
    var $percentChart = $("#myChart");
    var $percentChart1 = $("#myChart1");
    var $percentChart2 = $("#myChart2");
    var $percentChart3 = $("#myChart3");
    $.ajax({
        url: $chartsContainer.data("url"),
        success: function (data) {

            var ctx = $percentChart[0].getContext("2d");
            var ctx1 = $percentChart1[0].getContext("2d");
            var ctx2 = $percentChart2[0].getContext("2d");
            var ctx3 = $percentChart3[0].getContext("2d");

            new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Membres',
                        backgroundColor: [
                            '#4197CF', '#83D8A3', '#474747', '#C9CB9B', '#D3D3D3'
                          ],
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Dépenses en pourcentages'
                    }
                }
            });

            new Chart(ctx1, {
                type: 'doughnut',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Membres',
                        backgroundColor: [
                            '#B09D9C', '#822A16', '#474747', '#83D8A3', '#4197CF'
                          ],
                        data: data.amount
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Dépenses en Euros'
                    }
                }
            });

            new Chart(ctx2, {
                type: 'doughnut',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Membres',
                        backgroundColor: [
                            '#908190', '#522854', '#474747', '#83D8A3', '#4197CF'
                          ],
                        data: data.wages
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Revenus en Euros'
                    }
                }
            });

            new Chart(ctx3, {
                type: 'pie',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Membres',
                        backgroundColor: [
                            '#263238', '#90A4AE', '#455A64', '#607D8B', '#455A64'
                          ],
                        data: data.topay
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Parts de dépenses'
                    }
                }
            });

        }
    });

});