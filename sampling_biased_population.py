# pylint: disable=invalid-name
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import Script.distribution_population as dp

sns.set()


def main():

    """
    First, we get the information for the general population using the slider,
    We are using this information to generate the data using NumPy.
	Second, we select using slider the number of sampling and pass to the plot function,
    using Numpy to randomly select the population inside of the population.
    To see what is the difference in the population distribution when we sample in a representative
    and in a non-representative population.
    """

    st.sidebar.title("Parameters")

    # Getin all the general information using sliders
    total_population = st.sidebar.slider("Population Size", 0, 50000, 20000)

    st.sidebar.header("General Population Parameters")
    st.sidebar.markdown("Select the parameters you wish your general population have.")

    mean_population = st.sidebar.slider("Mean Population", 120, 200, 140)
    sd_population = st.sidebar.slider("Desviation Population", 0.1, 10.0, 5.0)
    probability_gym = st.sidebar.slider(
        "Probability person go to the gym %", 0.0, 100.0, 50.0
    )

    st.sidebar.header("Select Gym Population Parameters")
    st.sidebar.markdown("Select the parameters you wish your gym population have.")

    mean_gym = st.sidebar.slider("Mean Gym Population", 120, 200, 170)
    sd_gym = st.sidebar.slider("Desviation Gym Population", 0.1, 10.0, 5.0)

    st.title("Biased Population")

    st.markdown(
        " The main idea of the project is to see in a visual way how we sampling a population can change the mean we get. First, you need yo select the mean of the weight a person can lift and distribution for the general population. Second, you need to select the mean of the weight of a person that goes to the gym can lift, deviation, and the probability that a person of the general population goes to the gym.",
        unsafe_allow_html=True,
    )

    # Method to generate the random information using mean and distribution
    student_population = dp.biased_population(
        total_population, mean_population, sd_population, probability_gym,
    )

    gym_population = dp.biased_population(
        total_population, mean_gym, sd_gym, probability_gym, "gym"
    )

    population = np.append(student_population, gym_population)

    # Plot the general population
    plotGeneralPopulation(population, student_population, gym_population)

    st.title("Differents Effects of Sampling")

    # Sampling size to the population an the non representative population
    number_samples = st.slider("Number of Samples on the Population", 1, 10000, 5000)
    sample_size = st.slider("Size of each sample", 1, 100, 50)
    st.markdown("---")

    # Plots of sub population general and sub polulation gym
    subPlotPopulation(number_samples, sample_size, population)

    subPlotGymPopulation(number_samples, sample_size, gym_population, population)

    st.write(
        "This project is inspired by the course Statistics with Python by the University of Michigan available on Coursera"
    )

    st.markdown(
        'Made with *Love!*  <a href="https://github.com/serdubon"> <img src="https://img.icons8.com/material-rounded/24/000000/github.png"/> </a> :heartbeat:',
        unsafe_allow_html=True,
    )


def plotGeneralPopulation(population, student_population, gym_population):
    plt.figure(figsize=(10, 12))

    plt.subplot(212)
    plt.subplots_adjust(wspace=0.25, hspace=0.3)
    sns.distplot(population, bins=100)
    plt.xlabel("Weight (lbs)", size=20)
    plt.title("Total Population Distribution", size=15)
    plt.axvline(
        x=np.mean(population), ls="--", C="black", label="Mean Total Population"
    )
    plt.xlim([110, 200])
    plt.legend(fontsize=15)

    plt.subplot(221)
    sns.distplot(student_population)
    plt.title("Distribution Students Only", size=16)
    plt.xlabel("Weight (lbs)", size=15)
    plt.xlim([110, 200])

    plt.subplot(222)
    sns.distplot(gym_population)
    plt.title("Distritubion of Students that go to the Gym", size=16)
    plt.xlabel("Weight (lbs)", size=15)
    plt.xlim([110, 200])

    st.pyplot()


def subPlotPopulation(number_samples, sample_size, population):
    st.title("Sample Entire Population")

    st.markdown(
        "If we sampling the entire population we can get unbiased results, the mean of the total population is the same as the mean of the sampling population. This is because we use a  simple random sample (SRS) so every person has the same probability of bean chose and doesn't sample on a specific part of the population."
    )

    unbias_population = dp.distribution(number_samples, sample_size, population)

    plt.subplot(211)
    plt.subplots_adjust(wspace=0.25, hspace=0.3)
    sns.distplot(population, bins=100)
    plt.title("Total Population", size=19)
    plt.xlabel("Weight (lbs)", size=15)
    plt.axvline(
        np.mean(population), ls="--", color="black", label="Mean Total Population"
    )
    plt.xlim([110, 200])
    plt.legend(fontsize=15)

    plt.subplot(212)
    sns.distplot(unbias_population, bins=50)
    plt.title("Unbiased Population ", size=19)
    plt.xlabel("Weight (lbs)", size=15)
    plt.axvline(
        np.mean(unbias_population),
        ls="--",
        color="black",
        label="Mean Sample Population",
    )
    plt.xlim([110, 200])
    plt.legend(fontsize=15)
    st.pyplot()


def subPlotGymPopulation(number_samples, sample_size, gym_population, population):
    st.title("Sample Gym Population")

    st.markdown(
        "If we make the same number of sampling but this time we go to the gym to get results. We are going to get biased results, this is because we select a non-representative population and we can see that the distribution is biased."
    )
    biased_population = dp.distribution(number_samples, sample_size, gym_population)

    plt.subplot(211)
    plt.subplots_adjust(wspace=0.25, hspace=0.3)
    sns.distplot(population, bins=100)
    plt.title("Total Population", size=19)
    plt.xlabel("Weight (lbs)", size=15)
    plt.axvline(
        x=np.mean(population), ls="--", color="black", label="Mean Total Population"
    )
    plt.xlim([100, 200])
    plt.legend(fontsize=15)

    plt.subplot(212)
    sns.distplot(biased_population, bins=50)
    plt.title("Biased Population", size=19)
    plt.xlabel("Weight (lbs)", size=15)
    plt.axvline(
        np.mean(population),
        ls="--",
        zorder=0,
        color="black",
        label="Mean Total Population",
    )
    plt.axvline(np.mean(biased_population), ls="--", label="Mean Biased Population")
    plt.xlim([100, 200])
    plt.legend(fontsize=15)

    st.pyplot()


if __name__ == "__main__":
    main()
