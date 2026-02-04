import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import logo from './logo.png';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function Home() {
  return (
    <div className="container mt-4">
      <div className="row">
        <div className="col-lg-8 mx-auto text-center">
          <h1 className="display-4 mb-3">Welcome to OctoFit Tracker</h1>
          <p className="lead mb-4">Track your fitness activities, compete with teams, and achieve your goals!</p>
        </div>
      </div>
      
      <div className="row mt-4">
        <div className="col-md-6 col-lg-4 mb-4">
          <Link to="/users" className="text-decoration-none">
            <div className="card text-center h-100 shadow-sm" style={{ cursor: 'pointer', transition: 'transform 0.2s' }} 
                 onMouseEnter={(e) => e.currentTarget.style.transform = 'translateY(-5px)'}
                 onMouseLeave={(e) => e.currentTarget.style.transform = 'translateY(0)'}>
              <div className="card-body">
                <h5 className="card-title">👥 Users</h5>
                <p className="card-text">View all registered members and their profiles</p>
                <span className="btn btn-primary">View Users</span>
              </div>
            </div>
          </Link>
        </div>
        <div className="col-md-6 col-lg-4 mb-4">
          <Link to="/activities" className="text-decoration-none">
            <div className="card text-center h-100 shadow-sm" style={{ cursor: 'pointer', transition: 'transform 0.2s' }}
                 onMouseEnter={(e) => e.currentTarget.style.transform = 'translateY(-5px)'}
                 onMouseLeave={(e) => e.currentTarget.style.transform = 'translateY(0)'}>
              <div className="card-body">
                <h5 className="card-title">🏃 Activities</h5>
                <p className="card-text">See recent fitness activities and progress</p>
                <span className="btn btn-info">View Activities</span>
              </div>
            </div>
          </Link>
        </div>
        <div className="col-md-6 col-lg-4 mb-4">
          <Link to="/teams" className="text-decoration-none">
            <div className="card text-center h-100 shadow-sm" style={{ cursor: 'pointer', transition: 'transform 0.2s' }}
                 onMouseEnter={(e) => e.currentTarget.style.transform = 'translateY(-5px)'}
                 onMouseLeave={(e) => e.currentTarget.style.transform = 'translateY(0)'}>
              <div className="card-body">
                <h5 className="card-title">👥 Teams</h5>
                <p className="card-text">Browse and join fitness teams</p>
                <span className="btn btn-success">View Teams</span>
              </div>
            </div>
          </Link>
        </div>
        <div className="col-md-6 col-lg-4 mb-4">
          <Link to="/leaderboard" className="text-decoration-none">
            <div className="card text-center h-100 shadow-sm" style={{ cursor: 'pointer', transition: 'transform 0.2s' }}
                 onMouseEnter={(e) => e.currentTarget.style.transform = 'translateY(-5px)'}
                 onMouseLeave={(e) => e.currentTarget.style.transform = 'translateY(0)'}>
              <div className="card-body">
                <h5 className="card-title">🏆 Leaderboard</h5>
                <p className="card-text">Check the top performers and compete</p>
                <span className="btn btn-warning">View Leaderboard</span>
              </div>
            </div>
          </Link>
        </div>
        <div className="col-md-6 col-lg-4 mb-4">
          <Link to="/workouts" className="text-decoration-none">
            <div className="card text-center h-100 shadow-sm" style={{ cursor: 'pointer', transition: 'transform 0.2s' }}
                 onMouseEnter={(e) => e.currentTarget.style.transform = 'translateY(-5px)'}
                 onMouseLeave={(e) => e.currentTarget.style.transform = 'translateY(0)'}>
              <div className="card-body">
                <h5 className="card-title">💪 Workouts</h5>
                <p className="card-text">Explore suggested workout plans</p>
                <span className="btn btn-danger">View Workouts</span>
              </div>
            </div>
          </Link>
        </div>
      </div>
      
      <div className="row mt-4">
        <div className="col-lg-8 mx-auto">
          <div className="alert alert-info" role="alert">
            <h4 className="alert-heading">🚀 Getting Started</h4>
            <p>Welcome to your fitness journey! Use the navigation menu above or click the cards to explore:</p>
            <hr />
            <ul className="mb-0">
              <li>Track your daily activities and monitor progress</li>
              <li>Join teams and compete with friends</li>
              <li>Follow personalized workout plans</li>
              <li>Climb the leaderboard and earn achievements</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            <img src={logo} alt="OctoFit Logo" />
            OctoFit Tracker
          </Link>
          <button 
            className="navbar-toggler" 
            type="button" 
            data-bs-toggle="collapse" 
            data-bs-target="#navbarNav" 
            aria-controls="navbarNav" 
            aria-expanded="false" 
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link" to="/">Home</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/users" element={<Users />} />
        <Route path="/activities" element={<Activities />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/workouts" element={<Workouts />} />
      </Routes>
    </div>
  );
}

export default App;
