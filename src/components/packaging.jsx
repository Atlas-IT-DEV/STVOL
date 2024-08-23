import upakovka1 from "../images/packaging.png";

const Packaging = ({ packaging = upakovka1, name = "Упаковка", price = 300 }) => {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <img src={packaging} alt="" width={87} height={89}/>
      <p
        style={{ marginTop: 12, color: "rgba(175, 175, 175, 1)", fontSize: 18 }}
      >
        {name}
      </p>
      <p
        style={{ marginTop: 3, color: "rgba(175, 175, 175, 1)", fontSize: 18 }}
      >
        {price} ₽
      </p>
    </div>
  );
};

export default Packaging;
