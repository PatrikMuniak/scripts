
//
// class Spinner extends React.Component {
//   render() {
//     return (
//       <div class="spinner">
//         <div class="lds-ring">
//           <div></div>
//           <div></div>
//           <div></div>
//           <div></div>
//         </div>
//       </div>
//     );
//   };
// };
//
// ReactDOM.render(
//   <Spinner/>,
//   document.getElementById('container')
// );
class HelloMessage extends React.Component {
  render() {
    return (
      <div>
        Hello {this.props.name}
      </div>
    );
  }
}

ReactDOM.render(
  <HelloMessage name="Taylor" />,
  document.getElementById('hello-example')
);
