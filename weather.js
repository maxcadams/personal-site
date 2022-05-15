/*      Weather API and search bar     */

fetch('https://www.metaweather.com/api/location/search/?query=london', {
    //mode: 'no-cors'
}).then(res => console.log(res))
  .catch(error => console.log('ERROR'))
