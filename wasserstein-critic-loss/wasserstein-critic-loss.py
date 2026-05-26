import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Write code here
    real_scores = np.asarray(real_scores)
    fake_scores = np.asarray(fake_scores)
    E_real_scores = np.mean(real_scores)
    E_fake_scores = np.mean(fake_scores)
    print(E_fake_scores)
    print(E_real_scores)
    return E_fake_scores - E_real_scores