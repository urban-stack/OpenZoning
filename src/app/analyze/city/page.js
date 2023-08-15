// pages/AnotherPage.js
import Head from "next/head";
import Navbar from "../../../components/Navbar"; // Adjust the path based on your directory structure

export default function ChooseACity() {
  // Define the cities for the list
  const cities = [
    { name: "New York", url: "newyork" },
    { name: "Los Angeles", url: "losangeles" },
    { name: "Chicago", url: "chicago" },
    { name: "Houston", url: "houston" },
    { name: "Phoenix", url: "phoenix" },
    { name: "Philadelphia", url: "philadelphia" },
    { name: "San Antonio", url: "sanantonio" },
    { name: "San Diego", url: "sandiego" },
    { name: "Dallas", url: "dallas" },
    { name: "San Jose", url: "sanjose" },
  ];

  return (
    <div className="min-h-screen bg-gray-100">
      <Head>
        <link
          href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&display=swap"
          rel="stylesheet"
        />

        <title>Choose a city</title>
      </Head>

      {/* Navbar */}

      <Navbar activeLink={0} />

      {/* Main Content */}
      <div className="container mx-auto grid grid-cols-5 gap-4 mt-10 pl-12 pr-16">
        {/* Left Side (40%) */}
        <div className="col-span-2 p-4 border-r-2 border-black flex flex-col">
          <h1 className="text-6xl font-bold mb-8">ANALYZE</h1>
          <h2 className="text-3xl mb-2">What is this tool for?</h2>
          <p className="text-lg mb-2">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit
            amet tincidunt enim. Nulla facilisi. Nulla facilisi. Nulla facilisi.
            Nulla facilisi. Nulla facilisi. Nulla facilisi. Nulla facilisi.
            Nulla facilisi. Nulla facilisi. Nulla facilisi. Nulla facilisi.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Doloremque
            commodi id ratione, fugiat hic in! Architecto, repellendus nulla!
            Eos quidem molestias commodi quas ipsa animi, tempora molestiae cum
            ratione excepturi! Lorem ipsum dolor sit amet consectetur
            adipisicing elit. Quo iste nisi earum sit voluptatibus magni, odit
            rerum dolorum?
          </p>
        </div>

        {/* Right Side (60%) */}
        <div className="col-span-3 p-4   flex flex-col items-center">
          <h3 className="text-lg mb-10 self-start">Choose a city</h3>

          {/* Scrollable List without Scrollbar */}
          <div
            className="overflow-auto h-44 mb-2 w-full scrollbar-hide"
            style={{
              width: "40.625rem",
              height: "26.75rem",
            }}
          >
            {cities.map((city, index) => (
              <a
                key={index}
                href={`/analyze/city/${city.url}`}
                className="outline-text block text-center font-mono text-6xl font-semibold leading-none opacity-70 hover:opacity-100 hover:scale-110 transition-all duration-300 ease-in-out"
                style={{
                  lineHeight: "110%",
                }}
              >
                {city.name}
              </a>
            ))}
            {/* Arrow Icon */}
          </div>
          <div className="mx-auto mb-2">
            <span>⬇</span> {/* Replace with your preferred icon */}
          </div>
          {/* Continue Button */}
          <button className="bg-black text-white rounded px-4 py-2 uppercase mt-auto">
            Continue
          </button>
        </div>
      </div>
    </div>
  );
}
