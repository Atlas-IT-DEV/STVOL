import {
  VStack,
  Grid,
  GridItem,
  Text,
  Button,
  Image,
  Stack,
  Link,
} from "@chakra-ui/react";
import "./main_page.css";
import LakePhoto from "../images/lake.jpg";
import MountainPhoto from "../images/mountain.jpg";
import RiverPhoto from "../images/river.jpg";
import WeatherPhoto from "../images/weather.jpg";
import ProfilePage from "./profile_page";
import { useNavigate } from "react-router";

const MainPage = () => {
  const navigate = useNavigate();
  return (
    <VStack width={"100%"} bgColor={"black"}>
      <Grid
        width={"100%"}
        templateRows="repeat(7, 1fr)"
        templateColumns="repeat(5, 1fr)"
      >
        <GridItem
          rowSpan={1}
          colSpan={5}
          border={"1px solid white"}
          display={"flex"}
          justifyContent={"center"}
          alignItems={"center"}
        >
          <Text color={"white"} fontSize={"50px"} textAlign={"center"}>
            STVOL
          </Text>
        </GridItem>
        <GridItem
          rowSpan={1}
          colSpan={2}
          border={"1px solid white"}
          borderLeft={"1px solid black"}
          display={"flex"}
          justifyContent={"center"}
          alignItems={"center"}
        >
          <Text color={"white"} fontSize={"26px"} textAlign={"center"}>
            каталог
          </Text>
        </GridItem>
        <GridItem
          rowSpan={1}
          colSpan={3}
          border={"1px solid white"}
          display={"flex"}
          justifyContent={"center"}
          alignItems={"center"}
        >
          <Button
            color={"black"}
            fontSize={"26px"}
            textAlign={"center"}
            height={"auto"}
          >
            следующий
          </Button>
        </GridItem>
        <GridItem rowSpan={1} colSpan={1} border={"1px solid white"}></GridItem>
        <GridItem rowSpan={1} colSpan={1} border={"1px solid white"}>
          <Image src={LakePhoto} alt="КАРТИНКА" color={"white"} />
        </GridItem>
        <GridItem
          rowSpan={1}
          colSpan={1}
          border={"1px solid white"}
          justifyContent={"center"}
          display={"flex"}
          alignItems={"center"}
        >
          <Stack
            border={"3px solid white"}
            borderRadius={"50%"}
            justifyContent={"center"}
            width={"80px"}
            height={"80px"}
          >
            <Text color={"white"} fontSize={"50px"} textAlign={"center"}>
              1
            </Text>
          </Stack>
        </GridItem>
        <GridItem
          rowSpan={2}
          colSpan={2}
          border={"1px solid white"}
          borderRight={"1px solid black"}
        >
          <Image src="" alt="БУКЕТ" color={"white"} />
        </GridItem>
        <GridItem rowSpan={1} colSpan={1} border={"1px solid white"}>
          <Image src={RiverPhoto} alt="КАРТИНКА" color={"white"} />
        </GridItem>
        <GridItem rowSpan={1} colSpan={1} border={"1px solid white"}></GridItem>
        <GridItem
          rowSpan={1}
          colSpan={1}
          border={"1px solid white"}
          display={"flex"}
          justifyContent={"center"}
          alignItems={"center"}
          flexDirection={"column"}
        >
          <Text color={"white"} fontSize={"26px"} textAlign={"start"}>
            Цена <br />
            букета:
          </Text>
          <Text color={"white"} fontSize={"26px"} textAlign={"start"}>
            1000 ₽
          </Text>
        </GridItem>
        <GridItem rowSpan={1} colSpan={1} border={"1px solid white"}>
          <Image src={MountainPhoto} alt="КАРТИНКА" color={"white"} />
        </GridItem>
        <GridItem rowSpan={1} colSpan={1} border={"1px solid white"}>
          <Image src={WeatherPhoto} alt="КАРТИНКА" color={"white"} />
        </GridItem>
        <GridItem
          rowSpan={1}
          colSpan={1}
          border={"1px solid white"}
          justifyContent={"center"}
          display={"flex"}
          alignItems={"center"}
        >
          <Stack
            border={"3px solid white"}
            borderRadius={"50%"}
            justifyContent={"center"}
            width={"80px"}
            height={"80px"}
          >
            <Text color={"white"} fontSize={"50px"} textAlign={"center"}>
              2
            </Text>
          </Stack>
        </GridItem>
        <GridItem
          rowSpan={2}
          colSpan={2}
          border={"1px solid white"}
          borderRight={"1px solid black"}
        >
          <Image src="" alt="БУКЕТ" color={"white"} />
        </GridItem>
        <GridItem
          rowSpan={2}
          colSpan={2}
          border={"1px solid white"}
          display={"flex"}
          flexDirection={"column"}
          justifyContent={"space-evenly"}
          alignItems={"center"}
        >
          <Button
            width={"80%"}
            fontSize={"26px"}
            onClick={() => navigate("/about")}
          >
            что такое stvol?
          </Button>
          <Button
            width={"80%"}
            fontSize={"26px"}
            onClick={() => navigate("/constructor")}
          >
            конструктор
          </Button>
          <Button
            width={"80%"}
            fontSize={"26px"}
            onClick={() => navigate("/profile")}
          >
            Профиль
          </Button>
        </GridItem>
        <GridItem
          rowSpan={1}
          colSpan={1}
          border={"1px solid white"}
          display={"flex"}
          justifyContent={"center"}
          alignItems={"center"}
          flexDirection={"column"}
        >
          <Text color={"white"} fontSize={"26px"} textAlign={"start"}>
            Цена <br />
            букета:
          </Text>
          <Text color={"white"} fontSize={"26px"} textAlign={"start"}>
            2000 ₽
          </Text>
        </GridItem>
        <GridItem
          rowSpan={1}
          colSpan={3}
          border={"1px solid white"}
          display={"flex"}
          justifyContent={"center"}
          alignItems={"center"}
        >
          <Button
            color={"black"}
            fontSize={[20, 25, 30, 35, 40]}
            textAlign={"center"}
            height={"auto"}
          >
            предыдущий
          </Button>
        </GridItem>
      </Grid>
    </VStack>
  );
};
export default MainPage;
