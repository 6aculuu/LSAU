t = linspace(-5, 5, 20000);
phi = (exp(t)-1)/(exp(t)+1);
mu1 = 0*t;
mu2 = 1/2*t;
figure;
hold on;
plot(t, phi, LineWidth=2);
plot(t, mu1, LineWidth=2);
plot(t, mu2, LineWidth=2);
legend('$$\varphi(\sigma)=arctan(2\sigma)$$', '$$0$$', '$$\mu_0=2$$', 'Interpreter', 'latex');
xlabel('$$\sigma$$', 'Interpreter', 'latex');
ylabel('$$\varphi(\sigma)$$', 'Interpreter', 'latex');
grid on;
hold off;
