"use client";
import React, { useState, useEffect, useRef } from "react";
import L from "leaflet";
import shp from "shpjs";

const MapComponent = ({
  shapefilePath = "/shapefiles/Future_Land_Use_and_Built_Form_2040.zip",
  geoJSONPath = "/geojsons/minnepolis/neighborhoods.geojson",
  setSelectedAreas,
}) => {
  const mapRef = useRef(null);
  const [selectedBoundaries, setSelectedBoundaries] = useState([]);
  const boundariesLayerGroupRef = useRef(null);

  useEffect(() => {
    if (!mapRef.current) {
      return;
    }

    const mapInstance = L.map(mapRef.current).setView([44.9778, -93.265], 13);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(
      mapInstance
    );

    if (geoJSONPath) {
      fetch(geoJSONPath)
        .then((response) => response.json())
        .then((geoJSON) => {
          const boundariesLayerGroup = L.geoJSON(geoJSON, {
            renderer: L.canvas(),
            style: (feature) => {
              // Check if the boundary is already selected
              const isSelected = selectedBoundaries.some(
                (boundary) =>
                  boundary.properties["OBJECTID"] ===
                  feature.properties["OBJECTID"]
              );
              return {
                color: isSelected ? "red" : "blue",
              };
            },
            onEachFeature: (feature, layer) => {
              layer.on("click", (event) => {
                const isSelected = selectedBoundaries.some(
                  (boundary) =>
                    boundary.properties["OBJECTID"] ===
                    feature.properties["OBJECTID"]
                );

                if (isSelected) {
                  setSelectedBoundaries((prevSelected) =>
                    prevSelected.filter(
                      (boundary) =>
                        boundary.properties["OBJECTID"] !==
                        feature.properties["OBJECTID"]
                    )
                  );
                } else {
                  setSelectedBoundaries((prevSelected) => [
                    ...prevSelected,
                    feature,
                  ]);
                }
              });
            },
          }).addTo(mapInstance);

          boundariesLayerGroupRef.current = boundariesLayerGroup;

          return () => {
            boundariesLayerGroup.eachLayer((layer) => {
              layer.off("click");
            });
          };
        });
    }

    return () => {
      if (mapInstance) {
        mapInstance.remove();
      }
    };
  }, [geoJSONPath, selectedBoundaries]);

  useEffect(() => {
    setSelectedAreas(selectedBoundaries);

    const layerGroup = boundariesLayerGroupRef.current;
    if (layerGroup) {
      layerGroup.eachLayer((layer) => {
        layerGroup.resetStyle(layer);
      });
    }
  }, [selectedBoundaries]);

  return <div ref={mapRef} style={{ height: "100%", width: "100%" }} />;
};

export default MapComponent;
