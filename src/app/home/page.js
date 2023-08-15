import Head from "next/head";
import Navbar from "../../components/Navbar"; // Adjust the path based on your directory structure

export default function HomePage() {
  const cardsData = [
    {
      heading: "Analyse",
      subHeading: "EXPLORE THE ZONING CODE",
      description:
        "This tool will allow you to filter at a neighborhood scale parcels according to their allowable units and size",
      image: "https://via.placeholder.com/300x200",
    },
    {
      heading: "Develop",
      subHeading: "EXPLORE THE ZONING CODE",
      description:
        "This tool will allow you to filter at a neighborhood scale parcels according to their allowable units and size",
      image: "https://via.placeholder.com/300x200",
    },
    {
      heading: "Contribute",
      subHeading: "EXPLORE THE ZONING CODE",
      description:
        "This tool will allow you to filter at a neighborhood scale parcels according to their allowable units and size",
      image: "https://via.placeholder.com/300x200",
    },
  ];

  return (
    <div className="min-h-screen bg-gray-100">
      <Head>
        <title>HomePage for Openzoning</title>
      </Head>

      {/* Navbar */}
      <Navbar activeLink={0} />

      {/* Cards */}
      <div className="container mx-auto mt-10 grid grid-cols-3 gap-4 px-12">
        {cardsData.map((card, index) => (
          <div
            key={index}
            className="container bg-white p-12 rounded shadow flex flex-col"
          >
            {/* Heading */}
            <h2 className="text-xl text-gray-500 font-bold mb-4 mx-auto">
              {card.heading}
            </h2>

            {/* Logo */}
            <div className="h-48 mb-4 ">{card.image}</div>

            {/* Sub Heading */}
            <h3 className="text-lg mb-4">{card.subHeading}</h3>

            {/* Description */}
            <p className="text-sm mb-2">{card.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
