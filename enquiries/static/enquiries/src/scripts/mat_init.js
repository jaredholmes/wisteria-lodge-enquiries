document.addEventListener('DOMContentLoaded', function() {
  var elSideNav = document.querySelector('.sidenav');
  var instanceSideNav = M.Sidenav.init(elSideNav);

  var elSlider = document.querySelector('.slider');
  var instanceSlider = M.Slider.init(elSlider, { height: 650, interval: 4500 });

  var elMB = document.querySelector('.materialboxed');
  var instanceMB = M.Materialbox.init(elMB);

  var elDP = document.querySelectorAll('.datepicker');
  var instanceDP = M.Datepicker.init(elDP);

  var elemSel = document.querySelectorAll('select');
  var instanceSel = M.FormSelect.init(elemSel);
});
