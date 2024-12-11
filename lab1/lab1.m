% close all
% % Допустим, что результаты симуляции содержатся в переменной out
% % out.y - это результат симуляции, содержащий значения y и соответствующее время
% 
% % Получаем данные
% time = out.y_1.Time; % Время симуляции
% y_1 = out.y.Data;    % Значения y
% y_2 = out.y_2.Data;    % Значения y
% % u_1 = out.u_1.Data;    % Значения y
% u_2 = out.u_2.Data;    % Значения y
% u_1 = ones(size(time));
% 
% % Построение графика y(t) в отдельном окне
% figure;
% plot(time, y_1(:,1:1), 'r', 'LineWidth', 2, 'DisplayName','управляемая форма');
% hold on
% plot(time, y_2(:,1:1), 'b', 'LineWidth', 2, 'DisplayName','наблюдаемая форма');
% % plot(time, y_(:,1:1), 'r*', 'LineWidth', 0.5, 'DisplayName','bar');
% hold off
% title('y(t)');
% xlabel('t, с'); % Подпись оси x
% ylabel('y(t)');      % Подпись оси y
% grid on;
% legend('y_1(t)', 'y_2(t)', 'Location', 'northeast'); % Добавление легенды
% % % Построение графика y(t) в отдельном окне
% % figure;
% % plot(time, y_1(:,1:1), 'r', 'LineWidth', 0.5, 'DisplayName','bar');
% % hold off
% % title('y(t) диагональная форма');
% % xlabel('t, с'); % Подпись оси x
% % ylabel('y(t)');      % Подпись оси y
% % grid on;
% % legend('управляемая форма', 'наблюдаемая форма', 'диагональная форма', 'Location', 'best'); % Добавление легенды
close all
% Допустим, что результаты симуляции содержатся в переменной out
% out.y - это результат симуляции, содержащий значения y и соответствующее время

% Получаем данные
time = out.y.Time; % Время симуляции
y_1 = out.y.Data;    % Значения y
y_2 = y_1;    % Значения y
% u_1 = out.u_1.Data;    % Значения y
y_3 = y_1;   % Значения y
y_4 = y_1;
u_1 = ones(size(time));

% Построение графика y(t) в отдельном окне
figure;
plot(time, y_1(:,1:1), 'b', 'LineWidth', 2, 'DisplayName','управляемая форма');
hold on
plot(time, y_2(:,1:1), 'g--', 'LineWidth', 2, 'DisplayName','наблюдаемая форма');
plot(time, y_3(:,1:1), 'y:', 'LineWidth', 2, 'DisplayName','наблюдаемая форма');
plot(time, y_4(:,1:1), 'r*', 'LineWidth', 0.5, 'DisplayName','наблюдаемая форма');
% plot(time, y_(:,1:1), 'r*', 'LineWidth', 0.5, 'DisplayName','bar');
hold off
title('y(t)');
xlabel('t, с'); % Подпись оси x
ylabel('y(t)');      % Подпись оси y
grid on;
legend('управляемая форма', 'наблюдаемая форма', 'передаточная функция', 'диагональная форма', 'Location', 'northeast'); % Добавление легенды
% % Построение графика y(t) в отдельном окне
% figure;
% plot(time, y_1(:,1:1), 'r', 'LineWidth', 0.5, 'DisplayName','bar');
% hold off
% title('y(t) диагональная форма');
% xlabel('t, с'); % Подпись оси x
% ylabel('y(t)');      % Подпись оси y
% grid on;
% legend('управляемая форма', 'наблюдаемая форма', 'диагональная форма', 'Location', 'best'); % Добавление легенды

% % Построение графика u(t) в отдельном окне
% figure;
% plot(time, u_1(:,1:1), 'k', 'LineWidth', 2);
% hold on
% % plot(time, u_2(:,1:1), 'b', 'LineWidth', 2);
% title('u(t) u=1');
% xlabel('t, с'); % Подпись оси x
% ylabel('u(t)');      % Подпись оси y
% legend('u(t)', 'Location', 'southwest'); % Добавление легенды
% grid on;
