function getSensorReadings() {
    // fetch('https://jsonplaceholder.typicode.com/users')
    fetch('http://127.0.0.1:5000/get-sensor-readings')
    .then(response => response.json())
    .then(data => {
        refreshReadings(data);
    });
}

function refreshReadings(data) {
    // Remove recent rows
    const newRows = document.getElementsByClassName('recent-readings');
    Array.from(newRows).forEach(row => {
        row.remove();
    })

    // add new rows
    const myTable = document.getElementById('myTable');
    data.forEach(reading => {
        const table_row = document.createElement('tr');

        if (reading.value < -20 || reading.value > 15) table_row.classList.add('alert')

        table_row.classList.add('recent-readings');
        table_row.innerHTML = 
        '<td>' + reading.sensor_id +'</td>' +
        '<td>' + reading.sensor_type +'</td>' +
        '<td>' + reading.value +'</td>' +
        '<td>' + reading.time_stamp +'</td>';
    
        myTable.appendChild(table_row);
    });
}

setInterval(getSensorReadings, 3000)