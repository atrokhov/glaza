import React, { Component } from 'react';

class PageInsights extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: []
    };
  }

  componentDidMount() {
    fetch("http://api.glaza:8000/api/glaza/pageinsights?pagesize=4&sort=-date")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            items: result._embedded
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }

  render() {
    const { error, isLoaded, items } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {    
      return (
        <div>
          <ul>
            {items.map(item => (
              <li key={item.name}>
                <b>{item.name}</b> <span>{item.value}</span>
              </li>
            ))}
          </ul>
        </div>
      );
    }      
  }
}

export default PageInsights;