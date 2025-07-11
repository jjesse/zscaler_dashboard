# Database Initialization Script
# This script creates the initial database schema for the Mission Control Dashboard

-- Create database (if not exists)
-- Note: This is handled by Docker Compose environment variables

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_stat_statements";

-- Create schemas
CREATE SCHEMA IF NOT EXISTS public;
CREATE SCHEMA IF NOT EXISTS metrics;
CREATE SCHEMA IF NOT EXISTS audit;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    is_active BOOLEAN DEFAULT true,
    is_admin BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ZPA metrics table
CREATE TABLE IF NOT EXISTS metrics.zpa_metrics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    total_applications INTEGER,
    active_connectors INTEGER,
    total_users INTEGER,
    active_sessions INTEGER,
    threats_blocked INTEGER,
    policy_violations INTEGER,
    data JSONB
);

-- ZIA metrics table
CREATE TABLE IF NOT EXISTS metrics.zia_metrics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    total_requests BIGINT,
    blocked_requests BIGINT,
    allowed_requests BIGINT,
    bandwidth_used DECIMAL(10,2),
    malware_blocked INTEGER,
    phishing_blocked INTEGER,
    policy_violations INTEGER,
    data JSONB
);

-- ZDX metrics table
CREATE TABLE IF NOT EXISTS metrics.zdx_metrics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    overall_score DECIMAL(5,2),
    network_score DECIMAL(5,2),
    application_score DECIMAL(5,2),
    device_score DECIMAL(5,2),
    total_devices INTEGER,
    healthy_devices INTEGER,
    issues_detected INTEGER,
    data JSONB
);

-- Alerts table
CREATE TABLE IF NOT EXISTS alerts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    service VARCHAR(50) NOT NULL,
    severity VARCHAR(20) NOT NULL CHECK (severity IN ('critical', 'warning', 'info')),
    title VARCHAR(255) NOT NULL,
    message TEXT,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'resolved', 'dismissed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP WITH TIME ZONE,
    data JSONB
);

-- Audit log table
CREATE TABLE IF NOT EXISTS audit.activity_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    action VARCHAR(255) NOT NULL,
    resource VARCHAR(255),
    details JSONB,
    ip_address INET,
    user_agent TEXT,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Configuration table
CREATE TABLE IF NOT EXISTS configuration (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    key VARCHAR(255) UNIQUE NOT NULL,
    value JSONB,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_zpa_metrics_timestamp ON metrics.zpa_metrics(timestamp);
CREATE INDEX IF NOT EXISTS idx_zia_metrics_timestamp ON metrics.zia_metrics(timestamp);
CREATE INDEX IF NOT EXISTS idx_zdx_metrics_timestamp ON metrics.zdx_metrics(timestamp);
CREATE INDEX IF NOT EXISTS idx_alerts_service ON alerts(service);
CREATE INDEX IF NOT EXISTS idx_alerts_severity ON alerts(severity);
CREATE INDEX IF NOT EXISTS idx_alerts_status ON alerts(status);
CREATE INDEX IF NOT EXISTS idx_alerts_created_at ON alerts(created_at);
CREATE INDEX IF NOT EXISTS idx_activity_log_user_id ON audit.activity_log(user_id);
CREATE INDEX IF NOT EXISTS idx_activity_log_timestamp ON audit.activity_log(timestamp);

-- Create function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers for updated_at
CREATE TRIGGER update_users_updated_at 
    BEFORE UPDATE ON users 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_configuration_updated_at 
    BEFORE UPDATE ON configuration 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Insert default admin user (password: admin123 - CHANGE IN PRODUCTION!)
INSERT INTO users (username, email, hashed_password, full_name, is_admin) 
VALUES (
    'admin', 
    'admin@company.com', 
    '$2b$12$LqGCsWX2lzXLSEWNpDrQ3OzKJK5SaP6BvFLvYP8g.6wYDKp3YKn9e', -- admin123
    'System Administrator', 
    true
) ON CONFLICT (username) DO NOTHING;

-- Insert default configuration values
INSERT INTO configuration (key, value, description) VALUES
    ('dashboard_refresh_interval', '30', 'Dashboard refresh interval in seconds'),
    ('alert_retention_days', '90', 'Number of days to keep resolved alerts'),
    ('metrics_retention_days', '365', 'Number of days to keep metrics data'),
    ('enable_notifications', 'true', 'Enable email/slack notifications'),
    ('theme', '"dark"', 'Default dashboard theme')
ON CONFLICT (key) DO NOTHING;

-- Grant necessary permissions
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO mission_control;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA metrics TO mission_control;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA audit TO mission_control;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO mission_control;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA metrics TO mission_control;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA audit TO mission_control;
