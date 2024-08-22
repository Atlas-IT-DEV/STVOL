import flowers from "../images/buket1.png";

const Order = ({
  flower = flowers,
  date = "01.09.2001",
  name = "STVOL 18",
}) => {
  return (
    <div
      style={{ display: "flex", flexDirection: "column", alignItems: "center" }}
    >
      <img src={flower} alt="" />
      <p style={{ fontSize: 20, color: "rgba(67, 67, 67, 1)" }}>{date}</p>
      <p style={{ fontSize: 22, color: "rgba(175, 175, 175, 1)", borderBottom: "1px solid rgba(167, 167, 167, 1)"}}>{name}</p>
    </div>
  );
};

export default Order;
