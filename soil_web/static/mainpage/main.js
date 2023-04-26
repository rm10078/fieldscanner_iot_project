

var n,p,k,light,lightr,lightg,lightb,mos,tem,hum,timee;


function nav_but() {
    var x = document.getElementsByClassName("mobile_list")
    if (x[0].style.display === "none") {
        x[0].style.display = "flex";
    }
    else {
        x[0].style.display = "none"
    }
}

var a=document.getElementById("terget")
var id=a.textContent;
console.log(id)
const url = `/getdata?id=`+id;


setInterval(function(){ 
    //code goes here that will be run every 5 seconds.    
    fetch(url)
    .then(response => response.json())
    .then(data => {
        n = data.soiln;
        p = data.soilp;
        k = data.soilk;
        light = data.light;
        lightr = data.lightr;
        lightg = data.lightg;
        lightb = data.lightb;
        mos = data.soilmos;
        tem = data.tem;
        hum = data.hum;
        timee=data.time;
        // console.log("data recived")
    })
    .catch(error => console.error(error));

//soil n value
var sn = document.getElementById('soil_n').getContext('2d');
var chart_sn = new Chart(sn, {
    type: 'line',
    data: {
        labels: timee,
        datasets: [{
            label: 'My Dataset',
            backgroundColor: 'rgba(0, 213, 85, 0.301)',
            borderColor: 'rgb(0, 213, 85)',
            data: n
        }]
    },
    options: {}
});

//soil p value
var sp = document.getElementById('soil_p').getContext('2d');
var chart_sn = new Chart(sp, {
    type: 'line',
    data: {
        labels: timee,
        datasets: [{
            label: 'My Dataset',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255,99,132,1)',
            data: p
        }]
    },
    options: {}
});

//soil k value
var sk = document.getElementById('soil_k').getContext('2d');
var chart_sk = new Chart(sk, {
    type: 'line',
    data: {
        labels: timee,
        datasets: [{
            label: 'My Dataset',
            backgroundColor: 'rgba(0, 179, 255,0.3)',
            borderColor: 'rgb(0, 179, 255)',
            data: k
        }]
    },
    options: {}
});

//soil mos value
var smos = document.getElementById('soil_mos').getContext('2d');
var chart_smos = new Chart(smos, {
    type: 'line',
    data: {
        labels: timee,
        datasets: [{
            label: 'My Dataset',
            backgroundColor: 'rgba(157, 0, 255,0.3)',
            borderColor: 'rgb(157, 0, 255)',
            data: mos
        }]
    },
    options: {}
});

//soil light value
var slight = document.getElementById('soil_light').getContext('2d');
var chart_slight = new Chart(slight, {
    type: 'line',
    data: {
        labels: timee,
        datasets: [{
            label: 'My Dataset',
            backgroundColor: 'rgba(255, 0, 111,0.3)',
            borderColor: 'rgb(255, 0, 111)',
            data: light
        }]
    },
    options: {}
});

//soil tem value
var stem = document.getElementById('soil_tem').getContext('2d');
var chart_stem = new Chart(stem, {
    type: 'line',
    data: {
        labels: timee,
        datasets: [{
            label: 'My Dataset',
            backgroundColor: 'rgba(255, 255, 0,0.3)',
            borderColor: 'rgb(255, 255, 0)',
            data: tem
        }]
    },
    options: {}
});

//soil hum value
var shum = document.getElementById('soil_hum').getContext('2d');
var chart_shum = new Chart(shum, {
    type: 'line',
    data: {
        labels: timee,
        datasets: [{
            label: 'My Dataset',
            backgroundColor: 'rgba(128, 128, 128,0.5)',
            borderColor: 'rgb(0, 0, 0)',
            data: hum
        }]
    },
    options: {}
});
}, 10000);
