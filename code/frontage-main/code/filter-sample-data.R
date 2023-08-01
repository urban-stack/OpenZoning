library(sf)
library(tidyverse)
library(here)


# Create a polygon for a bounding box in minneapolis
bbox_poly <- tibble(lat = c(44.995661969064265,
                            45.01134975149715),
                    lon = c(-93.30790531104353,
                            -93.28365814129486)) |> 
  st_as_sf(coords = c("lon", "lat"), 
           crs = "WGS84") |> 
  st_transform(2812) |>
  st_bbox() |> 
  st_as_sfc()

all_parcels <- here("data",
                    "County_Parcels.geojson") |>
  st_read() |> 
  st_transform(2812)

all_streets <- here("data",
                    "Hennepin_County_Street_Centerlines.geojson") |>
  st_read() |> 
  st_transform(2812)

some_parcels <- all_parcels |>
  st_filter(bbox_poly) |>
  st_transform("WGS84")

some_streets <- all_streets |>
  st_filter(bbox_poly) |>
  st_transform("WGS84")

st_write(some_parcels,
         here("data",
              "test-parcels.geojson"),
         delete_dsn = TRUE)

st_write(some_streets,
         here("data",
              "test-streets.geojson"),
         delete_dsn = TRUE)
