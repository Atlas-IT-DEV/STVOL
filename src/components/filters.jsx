import Flowers from "./flowers";

const Filters = ({ nameFilter = "Летние букеты" }) => {
  return (
    <div>
      <p
        style={{
          fontSize: 27,
          color: "rgba(175, 175, 175, 1)",
          fontWeight: 800,
        }}
      >
        {nameFilter}
      </p>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(2, 1fr)",
          rowGap: 30,
          columnGap: 60,
        }}
      >
        <Flowers />
        <Flowers />
        <Flowers />
        <Flowers />
      </div>
    </div>
  );
};

export default Filters;
