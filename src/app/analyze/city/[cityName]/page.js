"use client";
import React, { useState } from "react";
import Navbar from "@/components/Navbar";

// import Navbar from "../../../components/Navbar";
import MapComponent from "@/components/MapComponent";
import { usePathname } from "next/navigation";

export default function MapPage(props) {
  let cityName = usePathname().split("/")[3];

  //   Capitalize the first letter of the city name
  cityName = cityName.charAt(0).toUpperCase() + cityName.slice(1);

  //   send the setSelectedBoundaries to the MapComponent and toggle it when the
  // user clicks on a boundary

  const [selectedAreas, setSelectedAreas] = useState([]);

  return (
    <div className="min-h-screen bg-gray-100">
      {/* <Navbar /> */}

      <div className="grid grid-cols-5 gap-4 h-screen text-white">
        <div
          className="col-span-2 ml-3  bg-oz-green p-4 rounded  flex flex-col rounded-r-[1.875rem] shadow"
          style={{ boxShadow: "0px 4px 4px 0px rgba(0, 0, 0, 0.25)" }}
        >
          <h1 className="text-4xl mb-4 font-semibold font-bahnschrift opacity-70 mt-[5rem]">
            AREA SELECTION
          </h1>
          <p className=" mt-5 ml-[5rem] mb-[5rem]">
            Already know which neighborhoods you would like to analyze? Great!
            Select the areas for your study and continue to the next screen.
          </p>
          <div className="inline-block">
            <h3 className="text-lg mb-4 font-semibold">SELECTION SUMMARY</h3>

            <div
              className="relative pl-8 border-2 overflow-hidden mb-4"
              style={{ background: "#1CA58B" }}
            >
              <div>
                <div className="absolute left-0 w-0.5 h-full mt-6 ml-[16px] bg-white bg-opacity-50"></div>
                <div className="relative p-4 flex items-center">
                  <div className="absolute left-0 w-2 h-2 mt-1.8 ml-[-20px] bg-white rounded-full"></div>
                  <h3 className="font-bold">City</h3>
                </div>
                <p className="text-black">{cityName}</p>
              </div>
              <div>
                <div className="relative p-4 mb-4 flex items-center">
                  <div className="absolute left-0 w-2 h-2 mt-1.8 ml-[-20px] bg-white rounded-full"></div>
                  <h3 className="font-bold">Area</h3>
                </div>
                <p className="text-black">
                  {/* do a map of selected Areas and print each of the elements seperated with a , */}
                  {console.log(selectedAreas)}
                  {selectedAreas.map((area, index) => {
                    return index == selectedAreas.length - 1 ? (
                      <span key={index}>{area["properties"]["BDNAME"]}</span>
                    ) : (
                      <span key={index}>
                        {area["properties"]["BDNAME"] + ", "}
                      </span>
                    );
                  })}
                </p>
              </div>
              {/* Add more timeline boxes as needed */}
            </div>

            <button
              className=" rounded px-8 py-2 uppercase mt-4 border-2"
              style={{ text: "#F0F2E9", borderColor: "#F0F2E9" }}
            >
              Continue
            </button>
          </div>
        </div>

        <div className="col-span-3 bg-white p-4 rounded shadow h-full">
          <MapComponent
            setSelectedAreas={setSelectedAreas}
            geoJSONPath="/geojsons/minnepolis/neighborhoods.geojson"
          />
        </div>
      </div>
    </div>
  );
}
