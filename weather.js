/*      Weather API and search bar     */

/* Process data
 * Input: JSON file from weatherapi.com
 * Outputs data onto HTML doc
 */
function procData(data) {

    let city = data['location']['name'];
    let country = data['location']['country'];

    /*for (const key in data) {
        console.log(key);
    }*/
    let mainContainer = document.getElementById('weather');
    let div = document.createElement('section_header');
    div.id = 'recent';
    div.innerHTML = 'City: ' + city + ' ' + 'Country: ' + country + '\n';
    mainContainer.appendChild(div);
}

function locationNotFound () {
    let mainContainer = document.getElementById('weather');
    let div = document.createElement('section_header');
    div.innerHTML = 'Location not Found\n';
    div.id = 'recent';
    mainContainer.appendChild(div);
}


function weatherapi(city) {
    fetch('https://api.weatherapi.com/v1/forecast.json?key=5d455582fdc545e39ae180540221505&q='.concat(city), {
        //mode: 'no-cors'
    }).then(res => {
        return res.json()
    })
        .then(data => procData(data))
        .catch(error => locationNotFound())
}

