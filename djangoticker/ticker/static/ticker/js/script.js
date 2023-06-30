var slider = document.getElementById("id_duration");
var output = document.getElementById("output");
output.innerHTML = slider.value + ' сек';

slider.oninput = function() {
    output.innerHTML = this.value + ' сек';
}