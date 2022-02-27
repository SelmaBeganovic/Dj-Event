import { FaSignInAlt, FaSignOutAlt } from "react-icons/fa";
import { useContext, useEffect } from "react";
import Link from "next/link";
import Search from "./Search";
import AuthContext from "@/context/AuthContext";
import styles from "@/styles/Header.module.css";

export default function Header() {
  const { user, logout } = useContext(AuthContext);

  const renderWhenUserIsLoggedIn = () => {
    return (
      <>
        <li>
          <Link href="/events/add">
            <a>Add Event</a>
          </Link>
        </li>
        <li>
          <Link href="/account/dashboard">
            <a>Dashboard</a>
          </Link>
        </li>
        <li>
          <button onClick={() => logout()} className="btn-secondary btn-icon">
            <FaSignOutAlt /> Logout
          </button>
        </li>
      </>
    );
  };

  const renderWhenUserIsNotLoggedIn = () => {
    return (
      <>
        <li>
          <Link href="/account/login">
            <a className="btn-secondary btn-icon">
              <FaSignInAlt /> Login
            </a>
          </Link>
        </li>
      </>
    );
  };

  return (
    <header className={styles.header}>
      <div className={styles.logo}>
        <Link href="/">
          <a>DJ Events</a>
        </Link>
      </div>

      <Search />

      <nav>
        <ul>
          <li>
            <Link href="/events">
              <a>Events</a>
            </Link>
          </li>
          {user ? renderWhenUserIsLoggedIn() : renderWhenUserIsNotLoggedIn()}
        </ul>
      </nav>
    </header>
  );
}
