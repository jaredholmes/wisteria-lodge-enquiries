var copyrightYear = (function () {
  var thisYear = new Date();
  var year = thisYear.getFullYear();

  document.getElementById('year').innerHTML = year;
}());
