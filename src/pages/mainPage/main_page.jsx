import styles from "../mainPage/main_page.module.css";

import { useNavigate } from "react-router";
import BottomMenu from "../../components/bottomMenu";
import { notificationIcon, telezhkaIcon } from "../../images/images";

const MainPage = () => {
  const navigate = useNavigate();
  return (
    <div className={styles.container}>
      <BottomMenu />
    </div>
  );
};
export default MainPage;
