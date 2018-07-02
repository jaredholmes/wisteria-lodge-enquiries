var gulp = require('gulp');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');
var pump = require('pump');

gulp.task('copyHTML', function() {
  return gulp.src('../../templates/enquiries/src/*.html')
    .pipe(gulp.dest('../../templates/enquiries/dist/'));
});

gulp.task('sass', function() {
  return gulp.src('src/stylesheets/*.sass')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('dist/stylesheets/'));
});

gulp.task('minify', function(cb) {
  pump([
      gulp.src('src/scripts/*.js'),
      uglify(),
      gulp.dest('dist/scripts/')
    ],
    cb
  );
});

gulp.task('watch', function() {
  gulp.watch('../../templates/enquiries/src/*.html', gulp.series('copyHTML'));
  gulp.watch('src/stylesheets/*.sass', gulp.series('sass'));
  gulp.watch('src/scripts/*.js', gulp.series('minify'));
});
