// components/Navbar.js

export default function Navbar({ activeLink }) {
  const logo = "LOGO";
  const icons = ["🔔", "⚙️", "👤"];
  const links = [
    { href: "#", label: "Tools" },
    { href: "#", label: "About Us" },
    { href: "#", label: "Glossory" },
  ];
  return (
    <nav className=" p-20 text-black flex justify-between items-center">
      {/* Logo */}
      <div>{logo}</div>

      {/* Navigation Links */}
      <div className="space-x-4">
        {links.map((link, index) => (
          <a key={index} href={link.href} className="hover:text-blue-300">
            {activeLink == index ? (
              <span className="border-y-2 border-black p-2 ">{link.label}</span>
            ) : (
              <>{link.label}</>
            )}
          </a>
        ))}
      </div>

      {/* Icons */}
      <div className="space-x-4">
        {icons.map((icon, index) => (
          <span key={index}>{icon}</span>
        ))}
      </div>
    </nav>
  );
}
