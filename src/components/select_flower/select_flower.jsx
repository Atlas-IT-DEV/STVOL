import styles from "./select_flower.module.css";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/grid";

// import "swiper/css/navigation";
import { FreeMode, Navigation, Grid } from "swiper/modules";
import FlowerCard from "../flower_card/flower_card";
import useWindowDimensions from "../hooks/windowDimensions";
import proteya from "./../../images/proteya.jpeg";
import chris from "./../../images/chris.jpeg";
import artishok from "./../../images/artishok.jpeg";

const SelectFlower = () => {
  const { width } = useWindowDimensions();
  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <Swiper
        style={{
          "--swiper-navigation-color": "rgba(167, 167, 167, 1)",
          "--swiper-navigation-size": "20px",
        }}
        className={styles.slideTrack}
        modules={[FreeMode, Navigation, Grid]}
        spaceBetween={36}
        freeMode={true}
        navigation={true}
        slidesPerView={3}
        grid={{ rows: 1, fill: "row" }}
      >
        <SwiperSlide className={styles.slider}>
          <FlowerCard image={artishok} name={"Артишок"} price={"-"} />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard image={chris} name={"Хризантема"} price={"-"} />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard image={proteya} name={"Протея"} price={"-"} />
        </SwiperSlide>
      </Swiper>
    </div>
  );
};

export default SelectFlower;
