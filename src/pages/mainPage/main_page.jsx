import styles from "../mainPage/main_page.module.css";

import { useNavigate } from "react-router";
import BottomBenu from "../../components/bottomMenu";
import { notificationIcon, telezhkaIcon } from "../../images/images";

const MainPage = () => {
  const navigate = useNavigate();
  return (
    <div className={styles.container}>
      <BottomBenu />
    </div>
  );
};
export default MainPage;
