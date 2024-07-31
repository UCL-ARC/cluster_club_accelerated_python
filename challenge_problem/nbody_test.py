import numpy as np

from nbody import calc_stable_orbit, generate_random_star_system, calc_acc


def test_calc_stable_orbit():

    (pos, vel) = calc_stable_orbit(np.ones(1), np.zeros(1))

    np.testing.assert_almost_equal(pos, np.array([0., 1.]).reshape(1, 2))
    np.testing.assert_almost_equal(vel, np.array([-1., 0.]).reshape(1, 2))

    (pos2, vel2) = calc_stable_orbit(np.ones(1), np.ones(1) * 2.0 * np.pi)

    np.testing.assert_almost_equal(pos, pos2)
    np.testing.assert_almost_equal(vel, vel2)

    (pos3, vel3) = calc_stable_orbit(np.ones(1), np.ones(1) * np.pi)

    np.testing.assert_almost_equal(pos, pos3 * -1.0)
    np.testing.assert_almost_equal(vel, vel3 * -1.0)


def test_generate_random_start_system():

    (pos, vel, mass) = generate_random_star_system(100)

    np.testing.assert_almost_equal(pos[0, :], 0.0)
    np.testing.assert_almost_equal(vel[0, :], 0.0)
    np.testing.assert_almost_equal(mass[0], 1.0)

    np.testing.assert_array_less(0.0, np.abs(pos[1:, :]))
    np.testing.assert_array_less(mass[1:], 1.0)


def test_calc_acc():

    mass = np.array([1.0, 1.0])
    pos = np.array([0.0, 0.0, 0.0, 0.0]).reshape(2, 2)
    acc = np.zeros_like(pos)

    calc_acc(acc, pos, mass)
    np.testing.assert_almost_equal(acc, 0.0)

    pos = np.array([1.0, 1.0, 0.0, 0.0]).reshape(2, 2)
    acc = np.zeros_like(pos)

    calc_acc(acc, pos, mass)
    epsilon = 1.1*np.power(len(pos), -0.48)
    np.testing.assert_almost_equal(np.abs(acc), (2 + epsilon**2)**-1.5)
    np.testing.assert_almost_equal(acc[0, :], acc[1, :] * -1.0)
