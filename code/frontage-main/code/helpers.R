library(tidyverse)
library(sf)

fun_bearing = function(my_line) {
  
  if(st_is_longlat(my_line)) {
    stop("Please use a projected coordinate system")
  }
  
  coords <- st_coordinates(my_line) |>
    as_tibble() |>
    group_by(L1) |>
    summarise(height = max(X) - min(X),
              width = max(Y) - min(Y)) |>
    mutate(bearing = atan(width/height)*180/pi)
  
  coords$bearing
  
}

fn_min_diff <- function(list_nums, num) {
  min(abs(num - unlist(list_nums)))
}
