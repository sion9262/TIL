import "./App.css"
import styled, { ThemeProvider } from "styled-components";
import GlobalStyle from "./GlobalStyled";

const Wrapper = styled.section`
  background-color: ${props => props.theme.bgColor};
  color: ${props => props.theme.color};
  padding: 4em;
  text-align: center;
`;

const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
`;
const theme = {
  bgColor: "black",
  color: "white"
}

function App() {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle/>
      <Wrapper>
        <Title>안녕하세요!</Title>
      </Wrapper>
    </ThemeProvider>
  );
}
export default App;
