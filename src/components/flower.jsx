import hrizantema from "../images/flower.png";

const Flower = ({ flower = hrizantema, name = "Цветок", price = 300 }) => {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <img src={hrizantema} alt="" />
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

export default Flower;
